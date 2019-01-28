"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Dalton Andrew.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.



import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()
    center_point1 = rg.Point(200, 200)
    center_point2 = rg.Point(200, 100)
    circle1 = rg.Circle(center_point1, 10)
    circle2 = rg.Circle(center_point2, 15)
    circle1.fill_color = 'blue'
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(500, 500)
    center_point = rg.Point(400, 400)
    center_pointx = 400
    center_pointy = 400
    circle = rg.Circle(center_point, 50)
    circle.attach_to(window)
    fill = 'blue'
    circle.fill_color = 'blue'
    outline = circle.outline_thickness = 3
    c1 = rg.Point(0, 0)
    c2 = rg.Point(300, 300)
    rectangle = rg.Rectangle(c1, c2)
    centerrect = rg.Point(150, 150)
    center1 = 150
    center2 = 150
    outline1 =rectangle.outline_thickness = 10
    rectangle.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    print(outline)
    print(fill)
    print(center_point)
    print(center_pointx)
    print(center_pointy)
    print(outline1)
    print('none')
    print(centerrect)
    print(center1)
    print(center2)


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.
    window = rg.RoseWindow(500, 500)
    start = rg.Point(10, 10)
    end = rg.Point(400, 10)
    midpoint = rg.Point(10, 195)
    x = 195
    y = 10
    line1 = rg.Line(start, end)
    line1.thickness = 5
    line1.attach_to(window)
    started = rg.Point(200, 200)
    ended = rg.Point(400, 200)
    line2 = rg.Line(started, ended)
    line2.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    print(midpoint)
    print(y)
    print(x)



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
