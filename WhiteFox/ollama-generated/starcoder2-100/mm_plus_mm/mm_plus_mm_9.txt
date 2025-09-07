
class Model(torch.nn.Module):
    def __init__(self, m1=None):
        super().__init__()
 
        if not m1:
            self.m1  = torch.nn.Conv2d(3,8,5)
        else:
            self.m1  = m1

        self.m2  = torch.nn.Linear(7*7*4096, 512)
 
    def forward(self, x):
        t1  = self.m1(x)
        t2  = self.m2(t1.view(800))
 
        return t2

# Initializing the model
m = Model()

 # Input tensor of the first module:
t1 = torch.randn(3, 5*7*4096).repeat_interleave(2)

 # Input tensors for the second module; The shape of each is 8 x (7*7*4096),  and the number of elements in this tensor is 5 * 7 * 4096.
t2 = torch.randn((3*5*7*4096).repeat(1))

 # Input tensors for the third module; The shape of each is 8 x (7*7*4096), and the number of elements in this tensor is 5 * 7 * 4096.
t3 = torch.randn((2*5*7*4096).repeat(1))

 # Input tensors for the fourth module; The shape of each is 8 x (7*7*4096), and the number of elements in this tensor is 5 * 7 * 4096.
t4 = torch.randn((3*2*7*4096).repeat(1))

 # Input tensors for the fifth module; The shape of each is 8 x (7*7*4096), and the number of elements in this tensor is 5 * 7 * 4096.
t5 = torch.randn((2*3*7*4096).repeat(1))

 # Inputs to the model; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fourth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fifth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fourth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fifth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fourth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fifth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fourth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fifth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fourth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fifth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fourth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fifth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fourth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fifth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fourth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fifth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fourth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the fifth module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the first module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the second module; The shape of each is (8 x 3, 5 * 7 * 4096), and the number of elements in this tensor is 5 * 7 * 4096.
x = torch.randn((2*8*7*4096).repeat(1))

 # Input tensors to the third module; The shape of each is (8 x 3