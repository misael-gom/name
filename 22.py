import turtle
import json

def draw_from_json(json_file):
    # configurar turtle
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(800, 800)
    t = turtle.Turtle()
    t.speed(0)
    screen.tracer(0)

    # cargar regiones
    with open(json_file) as f:
        regions = json.load(f)

    # calcular limites para centrar el dibujo
    all_points = [p for r in regions for p in r['contour']]
    min_x = min(p[0] for p in all_points)
    max_x = max(p[0] for p in all_points)
    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)

    # calcular escala y centro
    width = max_x - min_x
    height = max_y - min_y
    scale = min(600 / width, 600 / height)
    center_x = (max_x + min_x) / 2
    center_y = (max_y + min_y) / 2

    # dibujar regiones
    for region in regions:
        points = region['contour']
        color = '#{:02x}{:02x}{:02x}'.format(
            int(region['color'][0]),
            int(region['color'][1]),
            int(region['color'][2])
        )
        t.color(color, color)
        t.penup()

        # primer punto
        x = (points[0][0] - center_x) * scale
        y = (center_y - points[0][1]) * scale
        t.goto(x, y)
        t.pendown()
        t.begin_fill()

        # recorrer puntos
        for point in points[1:]:
            x = (point[0] - center_x) * scale
            y = (center_y - point[1]) * scale
            t.goto(x, y)

        # cerrar la figura
        t.goto((points[0][0] - center_x) * scale,
               (center_y - points[0][1]) * scale)
        t.end_fill()
        screen.update()

    screen.mainloop()

if __name__ == "__main__":
    draw_from_json("sunflowers.json")