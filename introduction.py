import flet as ft

def main(page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

ft.app(target=main)



# import flet as ft

# def main(page: ft.Page):
#     page.title = "Flet counter example"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     text_hello = ft.Text(value="Hello, world!", color="green")

#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()
    
#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()

#     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
#     page.add(
#         ft.Row(
#             [
#                 text_hello
#             ]
#         ),
#         ft.Row(
#             [
#                 ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.icons.ADD, on_click=plus_click)
#             ],
#             alignment=ft.MainAxisAlignment.CENTER
#         )
#     )

# ft.app(target=main)