import math
from .constants import *

class Vec3:
    """Class representing a 3D-Vector. Values are always stored as float
    """
    def __init__(self, *args, **kwargs):
        """
        Vec3 can be constructed the following way:

        v1 = Vec3(x,y,z)    # 3 integers or floats
        v2 = Vec3([x,y,z])  # from a list of 3 integers or floats
        v3 = Vec3((x,y,z))  # from a tuple of 3 integers or floats
        v4 = Vec3(x)

        # using named arguments
        v5 = Vec3(z=1)
        v6 = Vec3(x=1, y=2, z=3)
        v7 = Vec3(y=4, x=2)

        # using nothing (Null-Vector)
        v7 = Vec3()

        """

        if len(kwargs) == 0:
            if len(args) == 3:
                    self.x = float(args[0])
                    self.y = float(args[1])
                    self.z = float(args[2])
            elif len(args) == 1:
                if type(args) == tuple or type(args) == list:
                    self.x = float(args[0][0])
                    self.y = float(args[0][1])
                    self.z = float(args[0][2])
                else:
                    raise ValueError("Sequencial definition of Vec3 must be list or tuple!")

            elif len(args) == 0:
                self.x = self.y = self.z = 0.0

            else:
                raise ValueError("Wrong number of parameters in Vec3")
        else:

            if len(args) > 0:
                raise ValueError("Use keyword arguments OR normal arguments, both is not permitted")

            if "x" in kwargs:
                self.x = float(kwargs["x"])
            else:
                self.x = 0

            if "y" in kwargs:
                self.y = float(kwargs["y"])
            else:
                self.y = 0

            if "z" in kwargs:
                self.z = float(kwargs["z"])
            else:
                self.z = 0


    def __str__(self):
        """Convert vector to string
        """
        return "Vec3(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __add__(self, other):
        """add two vectors
        other: vector to add"""
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """subtract two vectors
        other: vector to subtract"""
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)


    def __eq__(self, other):
        if type(other) == list or type(other) == tuple:   # not checking type within tuple/list
            if len(other) == 3:
                return (abs(self.x - other[0]) < G_EPSILON) and (abs(self.y- other[1]) < G_EPSILON) and (abs(self.z - other[2]) < G_EPSILON)
            else:
                raise ValueError("Can't compare vector with list or tuple of length != 3")
        elif type(other) == Vec3:
            return (abs(self.x - other.x) < G_EPSILON) and (abs(self.y - other.y) < G_EPSILON) and (abs(self.z - other.z) < G_EPSILON)
        else:
            raise ValueError("Can't compare this type")


    def __mul__(self, s):
        if type(s) == Vec3:
            return Vec3(self.x * s.x, self.y * s.y, self.z * s.z)
        elif type(s) == float or type(s) == int:
            return Vec3(self.x * s, self.y * s, self.z * s)
        else:
            print("multiplicaton with wrong type")
            return Vec3(0.,0.,0.)

    def __rmul__(self, s):
        if type(s) == Vec3:
            return Vec3(self.x * s.x, self.y * s.y, self.z * s.z)
        elif type(s) == float or type(s) == int:
            return Vec3(self.x * s, self.y * s, self.z * s)
        else:
            print("multiplicaton with wrong type")
            return Vec3(0., 0., 0.)

    def __div__(self, s):
        if type(s) == Vec3:
            return Vec3(self.x / s.x, self.y / s.y, self.z / s.z)
        elif type(s) == float or type(s) == int:
            return Vec3(self.x / s, self.y / s, self.z / s)
        else:
            print("multiplicaton with wrong type")
            return Vec3(0., 0., 0.)

    def __rdiv__(self, s):
        if type(s) == Vec3:
            return Vec3(self.x / s.x, self.y / s.y, self.z / s.z)
        elif type(s) == float or type(s) == int:
            return Vec3(self.x / s, self.y / s, self.z / s)
        else:
            print("multiplicaton with wrong type")
            return Vec3(0., 0., 0.)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        else:
            raise IndexError("Vec3 has 3 components: [0] [1] and [2]")

    def __setitem__(self, key, value):
        if key == 0:
             self.x = float(value)
        elif key == 1:
            self.y = float(value)
        elif key == 2:
            self.z = float(value)
        else:
            raise IndexError("Vec3 has 3 components: [0] [1] and [2]")

    def copy(self):
        """
        :return: copy of current vector
        """
        return Vec3(self.x, self.y, self.z)

    def isZero(self):
        """
        :return: Truf if this is a zero-vector
        """
        return math.fabs(self.x) < G_EPSILON and math.fabs(self.y) < G_EPSILON and math.fabs(self.z) < G_EPSILON

    def length(self):
        """
        :return: return length of vector
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        """
        normalize this vector
        """
        l = self.length()
        if l != 0:
            self.x /= l
            self.y /= l
            self.z /= l


# Vector operations:
# ------------------

def cross(v1, v2):
    """Calculates cross product
    v1: vector
    v2: vector
    """
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Vec3(x, y, z)

def dot(a,b):
    """calculates the dot product"""
    return a.x * b.x + a.y * b.y + a.z * b.z


def normalize(v):
    """Returns the normalized vector without modifying the original vector"""
    l = v.length()
    if l != 0:
        return Vec3(v.x / l, v.y / l, v.z / l)
    else:
        return Vec3(0.0, 0.0, 0.0)


def reflect(N, I):
    """Reflects a vector
    N: Normal
    I: Incdient vector"""
    return I + N * (-2.0 * dot(N, I))


def faceforward(N, I):
    '''
    faceforward operation
    N: Normal vector
    I: Incident vector
    '''
    if dot(N, I) < 0:
        return N
    else:
        return -N


def refract(N, I, eta):
    '''
    refract operation
    N: Normal vector
    I: Incident vector
    eta: Refraction koefficient
    '''
    d = dot(I, N)
    k = 1 - eta * eta * (1 - d * d)
    if k < 0:
        return I
    else:
        return I * eta - N * (eta * d + math.sqrt(k))


def sign(v):
    def fsign(f):
        if f < 0:
            return -1
        if f > 0:
            return 1
        else:
            return 0

    return Vec3(fsign(v.x), fsign(v.y), fsign(v.z))


