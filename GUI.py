import FreeSimpleGUI as sg
import Functions as fn

label1 = sg.Text("Select file to compress:")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose")
output = sg.Text(key="output")

compress_button = sg.Button("Compress")

window =sg.Window("File Compressor",
          layout = [[label1,input1,button1],
          [label2, input2, button2],
          [compress_button, output]])
while True:
    events, values = window.read()
    print(events, values)
    filepaths = values["Choose"].split(";")
    destination = values["Choose0"]

    match events:
        case 'Compress':
            fn.make_archive(filepaths, destination )
            window["output"].update(value = "Compression was completed!")

window.close()