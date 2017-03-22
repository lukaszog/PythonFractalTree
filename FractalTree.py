import math
from random import randint

# const - upper limit for randint
s = 10

"""Simple fractal tree using SVG and recursion.

Usage:
    Create Root object bt Branch(x1=400, y1=800, x2=400, y2=600, color=60, size=35)
    x1, y1, x2, y2 - start points of root

    Generate Tree Tree(lenght=200, angle=-20, depth=9, x1=400, y1=600, size=35, color=60, outlist=resutlist)

    lenght - lenght of start branch
    angle - start angle of branch
    depth - number of tree level
    x1, y1 - start point of branch
"""


class Branch():
    """Class represents a single branch."""
    def __init__(self, x1, y1, x2, y2, color, size):
        """Assigning  values."""
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color
        self.size = size

    def __str__(self):
        """Return path SVG object with points, color and stroke of branch."""
        return '<path d="M {x1} {y1} L {x2} {y2}" stroke="rgb(100,{c},0)" stroke-width="{w}"/>\n'.format(
            x1=self.x1,
            y1=self.y1,
            x2=self.x2,
            y2=self.y2,
            w=self.size,
            c=self.color
        )

    def __repr__(self):
        """Return text represent object."""
        return self.__str__()


class Tree():
    """
    Class represents Tree.

    Tree is composed of Branch object.
    """
    def __init__(self, lenght, angle, depth, x1, y1, size, color, outlist):
        """Main point of start generation."""
        self.branches = self.drawbranch(lenght, angle, depth, x1, y1, size, color, outlist)

    def drawbranch(self, lenght, angle, depth, x1, y1, size, color, outlist):
        """Recursive function for generate three Branch object per iteration."""
        # if depth > 0
        if depth:
            # X value of second point
            x2 = x1 + lenght * math.cos(math.radians(angle))
            # Y value of second point
            y2 = y1 + lenght * math.sin(math.radians(angle))

            # modify lenght of single branch
            lenght = float(2.0 / 3.0 * lenght)
            # modify size of single branch
            size = float(2.0 / 3.0 * size) + 1
            # modify color of single branch
            color += 6

            # X value of B point
            bx = x1
            # Y value of B point
            by = y2

            # X value of C point
            cx = -x2 + 2 * x1
            # Y value of C point
            cy = y2

            # Create A point
            b1 = Branch(x1, y1, x2, y2, color, size)
            # Add to list
            outlist.append(str(b1))
            # Call drawbranch function (recursion)
            self.drawbranch(lenght, angle + randint(-10, s), depth - 1, x2, y2, size, color, outlist)

            # Create B point
            b2 = Branch(x1, y1, bx, by, color, size)
            # Add to list
            outlist.append(str(b2))
            # Calculate new angle
            nangle = angle + randint(-1, 0) * randint(1, s)
            # Call drawbranch function (recursion)
            self.drawbranch(lenght, nangle, depth - 1, bx, by, size, color, outlist)

            # Create C point
            b3 = Branch(x1, y1, cx, cy, color, size)
            # Add to list
            outlist.append(str(b3))
            # Calculate new angle
            nangle = angle + randint(0, 1) * randint(1, s)
            # Call drawbranch function (recursion)
            self.drawbranch(lenght, nangle, depth - 1, cx, cy, size, color, outlist)

        # Return list of branches
        return outlist

    def write_svg(self, output='drzewko.svg'):
        """Function that write all branches to SVG file."""
        with open(output, 'w') as outfile:
            # Write SVG declaration
            outfile.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" version="1.1">\n')
            # Map to str all branches and write it into file
            outfile.writelines(map(str, self.branches))
            # End of SVG file
            outfile.write('</svg>\n')


print "Start generating, please wait.."
# Create empty list
resutlist = []
# Create root of Tree and add to list
resutlist.append(Branch(x1=400, y1=800, x2=400, y2=600, color=60, size=35))

# Call Tree object
t = Tree(lenght=200, angle=-20, depth=9, x1=400, y1=600, size=35, color=60, outlist=resutlist)
# After generate tree save to file
t.write_svg()

print "Done, check SVG file"
