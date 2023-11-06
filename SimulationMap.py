from tkinter import *
import tkintermapview
from DijsktraAlgo import GetShortestPath

paths_list = []

routes_label_list = []

def GetCoordinates(routes): 

    raw_routes = []
    raw_coordinates = []

    
    for i in routes:
        if i == 'BFP':
            BFP = map_widget.set_marker(14.118062, 122.945806, text="BFP")
            BFPR1 = map_widget.set_marker(14.117622, 122.945908, text="") 

            raw_coordinates.append([14.118062, 122.945806]) 
            raw_coordinates.append([14.117622, 122.945908]) 
            
            raw_routes.append(BFP)
            raw_routes.append(BFPR1)

        if i == 'TOTAL':
            TOTAL = map_widget.set_marker(14.115620, 122.941004, text="Total")
            TOTALR1 = map_widget.set_marker(14.114174, 122.941746, text="") 
            raw_coordinates.append([14.115620, 122.941004]) 

            raw_routes.append(TOTAL)

        if i == 'GAHONON':
            GAHONON = map_widget.set_marker(14.1192071, 122.9504177, text="Gahonon")
        
            raw_coordinates.append([14.1192071, 122.9504177]) 

            raw_routes.append(GAHONON)


        if i == 'GREENVIEW':
            GREENVIEW = map_widget.set_marker(14.1111768, 122.9450618, text="Greenview")   
        
            raw_coordinates.append([14.114174, 122.941746]) 
            raw_coordinates.append([14.1111768, 122.9450618]) 

            raw_routes.append(TOTALR1)
            raw_routes.append(GREENVIEW)

        if i == 'IRAYA':
            IRAYAR1 = map_widget.set_marker(14.1122498, 122.9461457, text="")    
            IRAYAR2 = map_widget.set_marker(14.1119168, 122.9473044, text="")  
            IRAYAR3 = map_widget.set_marker(14.1135816, 122.9476048, text="")  
            IRAYA = map_widget.set_marker(14.1137273, 122.9459526, text="Iraya")   
        
            raw_coordinates.append([14.1122498, 122.9461457]) 
            raw_coordinates.append([14.1119168, 122.9473044]) 
            raw_coordinates.append([14.1135816, 122.9476048]) 
            raw_coordinates.append([14.1137273, 122.9459526]) 

            raw_routes.append(IRAYAR1)
            raw_routes.append(IRAYAR2)
            raw_routes.append(IRAYAR3)
            raw_routes.append(IRAYA)


        if i == 'SAMAKA':
            SAMAKAR1 = map_widget.set_marker(14.1103009, 122.9459915, text="")      
            SAMAKA = map_widget.set_marker(14.1096255, 122.9453269, text="Samaka")  

            raw_coordinates.append([14.1103009, 122.9459915])  #14.1103009 122.9459915
            raw_coordinates.append([14.1096255, 122.9453269])  

            raw_routes.append(SAMAKAR1) 
            raw_routes.append(SAMAKA) 

        if i == 'CAMAMBUGANP-1':
            CAMAMBUGANP1 = map_widget.set_marker(14.107145, 122.949019, text="Camambugan P-1")
        
            raw_coordinates.append([14.107145, 122.949019])  

            raw_routes.append(CAMAMBUGANP1) 

        if i == 'BIBIRAO':
            BIBIRAOR1 = map_widget.set_marker(14.1025505, 122.9530775, text="BR1")
            BIBIRAOR2 = map_widget.set_marker(14.1043611, 122.9477794, text="BR2")
            BIBIRAOR3 = map_widget.set_marker(14.1039296, 122.9407360, text="BR3")
            BIBIRAOR4 = map_widget.set_marker(14.1025791, 122.9390007, text="BR4")
            BIBIRAOR5 = map_widget.set_marker(14.1000401, 122.9354816, text="BIBIRAO")

            raw_coordinates.append([14.1025505, 122.9530775])
            raw_coordinates.append([14.1043611, 122.9477794])
            raw_coordinates.append([14.1039296, 122.9407360])
            raw_coordinates.append([14.1025791, 122.9390007])
            raw_coordinates.append([14.1000401, 122.9354816])  

            raw_routes.append(BIBIRAOR1) 
            raw_routes.append(BIBIRAOR2) 
            raw_routes.append(BIBIRAOR3) 
            raw_routes.append(BIBIRAOR4) 
            raw_routes.append(BIBIRAOR5) 

        if i == "ALAWIHAO":
            ALAWIHAOR1 = map_widget.set_marker(14.109158, 122.929057, text="")
            ALAWIHAOR2 = map_widget.set_marker(14.106762, 122.926053, text="")
            ALAWIHAOR3 = map_widget.set_marker(14.106046, 122.924161, text="")
            ALAWIHAO = map_widget.set_marker(14.106661, 122.917411, text="ALAWIHAO")

            raw_coordinates.append([14.109158, 122.929057])
            raw_coordinates.append([14.106762, 122.926053])
            raw_coordinates.append([14.106046, 122.924161])
            raw_coordinates.append([14.106661, 122.917411])  
            
            raw_routes.append(ALAWIHAOR1) 
            raw_routes.append(ALAWIHAOR2) 
            raw_routes.append(ALAWIHAOR3) 
            raw_routes.append(ALAWIHAO) 



    return raw_routes, raw_coordinates

def Set(destination):
    global specific_routes_label

    destination_routes, shortest_distance_path = GetShortestPath("BFP", destination)

    routes, coordinates = GetCoordinates(destination_routes)

    y_axis = 220
    for i in destination_routes:
        specific_routes_label = canvas.create_text(1020, y_axis, text=i, anchor='center', fill='white', font=('courier new', 10))
        y_axis+=30
        routes_label_list.append(specific_routes_label)

    canvas.itemconfig(routes_label, text=f"Routes: ")
    canvas.itemconfig(total_distance_label, text=f"Total Distance: {(shortest_distance_path)} meters")

    print(coordinates)

    for i in range(len(coordinates) - 1):
        path_1 = map_widget.set_path([routes[i].position, routes[i+1].position, coordinates[i]])

def RemoveCoordinates():
    map_widget.delete_all_path()
    map_widget.delete_all_marker()
    
    canvas.itemconfig(routes_label, text=f"")
    canvas.itemconfig(total_distance_label, text=f"")

    for i in routes_label_list:
        canvas.itemconfig(i, text=f"")


root = Tk()
root.title('Daet Map')
root.geometry('1200x700+50+0')

canvas = Canvas(root, width=1200, height=700, bg='#686362')
canvas.pack()

my_label = LabelFrame(root)
my_label.pack(pady=20)

label_text = "Simulation Map"
label = Label(canvas, text=label_text, bg='white', font=('Arial', 15)) 
label_window = canvas.create_window(450, 50, window=label)

text = "Details:"
canvas.create_text(930, 130, text=text, anchor='center', fill='white', font=('courier new', 12))
routes_label = canvas.create_text(925, 190, text="", anchor='center', fill='white', font=('courier new', 10))
total_distance_label = canvas.create_text(1000, 160, text="", anchor='center', fill='white', font=('courier new', 10))

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=500, corner_radius=0)
#map_widget.set_position(14.0996, 122.9550)

canvas.create_window(450, 360, window=my_label)

map_widget.set_address("Daet, Camarines Norte, Philippines")


map_widget.set_zoom(14)

map_widget.pack()


alawihao_btn = Button(my_label, text="Alawihao", command=lambda:Set('ALAWIHAO'))
alawihao_btn.pack(side="left")

gahonon_btn = Button(my_label, text="Gahonon", command=lambda:Set('GAHONON'))
gahonon_btn.pack(side="left")

camambuganp1_btn = Button(my_label, text="Camambugan P-1", command=lambda:Set('CAMAMBUGANP-1'))
camambuganp1_btn.pack(side="left")

camambuganp2_btn = Button(my_label, text="Camambugan P-2", command=lambda:Set('CAMAMBUGANP-2'))
camambuganp2_btn.pack(side="left")

greenview_btn = Button(my_label, text="Greenview", command=lambda:Set('GREENVIEW'))
greenview_btn.pack(side="left")

samaka_btn = Button(my_label, text="Samaka", command=lambda:Set('SAMAKA'))
samaka_btn.pack(side="left")

iraya_btn = Button(my_label, text="Iraya",  command=lambda:Set('IRAYA'))
iraya_btn.pack(side="left")

bibirao_btn = Button(my_label, text="Bibirao", command=lambda:Set('BIBIRAO'))
bibirao_btn.pack(side="left")

remove_coordinates_button = Button(root, text="Reset", background="black", fg="gold", width=10, height=2, command=RemoveCoordinates)
canvas.create_window(1130, 600, window=remove_coordinates_button)

root.mainloop()

