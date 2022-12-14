# š Hi, Iām @shariquetelco
# š Iām interested in Coding for Signal and Communication
# š± Iām currently learning anything and everything
# šļø Iām looking to collaborate on 5G and 6G
# š« How to reach me eshariq.am@gmail.com


import turtle as t
t.write("@Shariquetelco")

t.pensize(10)
t.fillcolor('yellow')
t.hideturtle()
t.bgcolor("#eeeeee")

radius = 180
t.penup()
t.setposition(0, -radius)
t.setheading(0)
t.pendown()
t.begin_fill()
t.circle(radius)
t.end_fill()

mouth_radius = radius * 0.6
mouth_angle = 70
t.penup()
t.setposition(0, -mouth_radius)
t.setheading(0)
t.pendown()
t.circle(mouth_radius, mouth_angle)
t.penup()
t.setposition(0, -mouth_radius)
t.setheading(0)
t.pendown()
t.circle(mouth_radius, -mouth_angle)

eye_x = 50
eye_y = 50
eye_size = 60
t.penup()
t.setposition(eye_x, eye_y)

t.pendown()
t.dot(eye_size)
t.penup()
t.setposition(-eye_x, eye_y)
t.pendown()
t.dot(eye_size)


t.done()