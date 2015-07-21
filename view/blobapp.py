#
# BlobEdit - A totally silly application for showing
#  ========   off the GUI framework and providing an example
#             of its use.
#
#  Blobs are red squares that you place on a Blob Document
#  by clicking and move around by dragging. You can save
#  your blob arrangement in a file and load it back later
#  to impress your friends (or send them away screaming).
#
#  News flash: Got a blob you don't want? Now you can
#  get rid of it by shift-clicking it! Isn't that useful!
#

import pickle
from GUI import Application, ScrollableView, Document, Window, Cursor, rgb, Font
from GUI.Files import FileType
from GUI.Geometry import pt_in_rect, offset_rect, rects_intersect
from GUI.StdColors import black, red, clear, green, white
from controller.game_actions import war

GRID_SIZE = 50


class BlobApp(Application):
    def __init__(self, board):
        Application.__init__(self)
        self.blob_type = FileType(name="Blob Document", suffix="blob",
                                  # mac_creator = "BLBE", mac_type = "BLOB", # These are optional
        )
        self.file_type = self.blob_type
        self.blob_cursor = Cursor("C:\\Python27\\lib\\site-packages\\GUI\\Resources\\cursors\\arrow.tiff")
        self.board = board

    def open_app(self):
        self.new_cmd()

    def make_document(self, fileref):
        return BlobDoc(file_type=self.blob_type)

    def make_window(self, document):
        win = Window(size=(1000, 1000), document=document)
        view = BlobView(model=document, extent=(1000, 1000), scrolling='hv',
                        cursor=self.blob_cursor)
        win.place(view, left=0, top=0, right=0, bottom=0, sticky='nsew')
        win.show()
        view.draw_grid(self.board)


class BlobView(ScrollableView):
    def draw_grid(self, board):
        x, y = 200, 200
        sx, sy = 100, 100
        plopped_regions = []

        def find_pos(x, y):
            for ny in range(-1, 2):
                for nx in range(-1, 2):
                    if not self.model.find_blob(nx * GRID_SIZE + x, ny * GRID_SIZE + y):
                        point = (nx * GRID_SIZE + x, ny * GRID_SIZE + y)
                        return point
            else:
                raise RuntimeError('raaape')

        def sort_rankings(r):
            d = []
            s = r.values()
            for c in sorted(s, reverse = True):
                for name, rank in r.iteritems():
                    if rank == c:
                        if name not in d:
                            d.append(name)
            return d



        drawn_continents = []
        for continent in board.get_world():
            if continent not in drawn_continents:
                drawn_continents.append(continent)
                for territory in board.get_world()[continent]['territories']:
                    if territory.get_name() not in plopped_regions:
                        pos = find_pos(x, y)
                        x = pos[0]
                        y = pos[1]
                        self.model.add_blob(Blob(x, y, territory))
                        plopped_regions.append(territory.get_name())
                    for connection in territory.get_connections():
                        if connection.get_name() not in plopped_regions and connection.get_continent() == continent:
                            pos = find_pos(x, y)
                            plopped_regions.append(connection.get_name())
                            self.model.add_blob(Blob(pos[0], pos[1], connection))
                    x = pos[0]
                    y = pos[1]
                x += GRID_SIZE * 10
                y = sy + GRID_SIZE *2

            ranked_continents = sort_rankings(board.get_world()[continent]['connecting_continents'])
            for x1 in range(0,len(ranked_continents)):
                if ranked_continents[x1] not in drawn_continents:
                    drawn_continents.append(ranked_continents[x1])
                    for territory in board.get_world()[ranked_continents[x1]]['territories']:
                        if territory.get_name() not in plopped_regions:
                            pos = find_pos(x, y)
                            x = pos[0]
                            y = pos[1]
                            self.model.add_blob(Blob(x, y, territory))
                            plopped_regions.append(territory.get_name())
                        for connection in territory.get_connections():
                            if connection.get_name() not in plopped_regions and connection.get_continent() == ranked_continents[x1]:
                                pos = find_pos(x, y)
                                plopped_regions.append(connection.get_name())
                                self.model.add_blob(Blob(pos[0], pos[1], connection))
                        x = pos[0]
                        y = pos[1]
                    x += GRID_SIZE * 10
                    y = sy + GRID_SIZE *2
        lista = []
        settet = set()
        for blob in self.model.blobs:
            lista.append(blob.get_territory())
            settet.add(blob.get_territory())
        print "Antal territorier utritade: " + str(len(lista))
        print "Antal unika territorier utritade: " + str(len([i for i in settet]))

    def draw(self, canvas, update_rect):
        canvas.erase_rect(update_rect)
        canvas.pencolor = black
        for blob in self.model.blobs:
            if blob.intersects(update_rect):
                canvas.fillcolor = blob.get_color()
                blob.draw(canvas)

    def mouse_down(self, event):
        x, y = event.position
        blob = self.model.find_blob(x, y)
        if blob:
            if not event.shift:
                print "Continent: " + blob.get_continent() + ". Connections are: " + blob.get_connections() + ". Owner is: " + blob.get_owner_name()
            else:
                self.drag_blob(blob, x, y)

    def drag_blob(self, blob, x0, y0):
        start_pos = blob.get_position()
        for event in self.track_mouse():
            x, y = event.position
            self.model.move_blob(blob, x - x0, y - y0)
            x0 = x
            y0 = y
        neighbour_territory = self.model.find_blob(x,y)
        if neighbour_territory:
            if neighbour_territory.get_owner_name() != blob.get_owner_name() and blob.get_soldiers() > 1:
                print war(blob.territory, neighbour_territory.territory, blob.get_soldiers()-1).get_owner()
                self.model.set_blob_position(blob,start_pos[0], start_pos[1])
            else:
                print "Attacking yourself, or territory has only 1 soldier."
                self.model.set_blob_position(blob,start_pos[0], start_pos[1])
        else:
            print "No target."
            self.model.set_blob_position(blob,start_pos[0], start_pos[1])

    def blob_changed(self, model, blob):
        self.invalidate_rect(blob.rect)


class BlobDoc(Document):
    blobs = None

    def new_contents(self):
        self.blobs = []

    def read_contents(self, file):
        self.blobs = pickle.load(file)

    def write_contents(self, file):
        pickle.dump(self.blobs, file)

    def add_blob(self, blob):
        self.blobs.append(blob)
        self.changed()
        self.notify_views('blob_changed', blob)

    def find_blob(self, x, y):
        for blob in self.blobs:
            if blob.contains(x, y):
                return blob
        return None

    def move_blob(self, blob, dx, dy):
        self.notify_views('blob_changed', blob)
        blob.move(dx, dy)
        self.changed()
        self.notify_views('blob_changed', blob)

    def set_blob_position(self, blob, dx, dy):
        self.notify_views('blob_changed', blob)
        blob.set_position(dx, dy)
        self.changed()
        self.notify_views('blob_changed', blob)

    def delete_blob(self, blob):
        self.notify_views('blob_changed', blob)
        self.blobs.remove(blob)
        self.changed()


class Blob:
    def __init__(self, x, y, territory_obj):
        self.rect = (x, y, x + GRID_SIZE, y + GRID_SIZE)
        self.territory_obj = territory_obj

    def contains(self, x, y):
        return pt_in_rect((x, y), self.rect)

    def get_position(self):
        pos = (self.rect[0],self.rect[1])
        return pos

    def intersects(self, rect):
        return rects_intersect(rect, self.rect)

    def move(self, dx, dy):
        self.rect = offset_rect(self.rect, (dx, dy))

    def set_position(self,dx,dy):
        self.rect = (dx,dy, dx + GRID_SIZE, dy + GRID_SIZE)

    def draw(self, canvas):
        canvas.fill_frame_rect(self.rect)
        canvas.moveto(self.rect[0] + 2, self.rect[1] + 14)
        font_size = 12
        f = Font("Times", font_size, [])
        canvas.font = f
        canvas.textcolor = black
        st = self.territory_obj.get_name().split('_')
        ny = self.rect[1] + 14
        for word in st:
            if canvas.fillcolor == black:
                canvas.textcolor = red
            canvas.show_text(word)
            ny += font_size
            canvas.moveto(self.rect[0] + 2, ny)
        canvas.moveto(self.rect[0] + (GRID_SIZE - 10 * len(str(self.get_soldiers()))), self.rect[1] + (GRID_SIZE - 3))
        canvas.show_text(str(str(self.territory_obj.get_soldiers())))


    def get_territory(self):
        return self.territory_obj.get_name()

    def get_soldiers(self):
        return self.territory_obj.get_soldiers()

    def get_continent(self):
        return self.territory_obj.get_continent()

    def get_connections(self):
        cn = [x.get_name() for x in self.territory_obj.get_connections()]
        return ", ".join(cn)

    def get_owner_name(self):
        return self.territory_obj.get_owner()

    def get_color(self):
        return self.territory_obj.get_color()

    @property
    def territory(self):
        return self.territory_obj

    @territory.setter
    def set_territory_obj(self):
        return self.territory_obj
