
class Model(torch.nn.Module):
    def __init__(self, num=20):
        super().__init__()
 
        # Setting the number of elements in each array to be equal to 'num'
        self._a = torch.randn(1, 1, 3).repeat_interleave(repeats=num, dim=1)
        self._b = torch.randn(1, num).repeat_interleave(repeats=20, dim=1)

        # Creating an empty array to hold the results of the matrix multiplication
        c = torch.zeros((1, 3))
 
    def forward(self):
 
        # Matrix multiplication between 'a' and 'b' 
        c[...]  = torch.mm(self._a, self._b)

        # Returning the result of performing matrix multiplication between 'a' and 'b',
        return c


# Initializing the model
m  = Model()


# Inputs to the model
__input1__  = 40, __input2__  = torch.randn(3*1)
__input3__  = 50, __input4__  = torch.randn(num=1, size=(3*2))

x1  = torch.cat((__input1__, __input2__), dim=1).repeat_interleave(__input3__, dim=2)
x2  = torch.cat((__input3__, __input4__), dim=1).repeat(repeats=1, __input1__).transpose(-1,-2)


__output__  = m(torch.randn(10))

# This model is different from the previous one (model 6), and it should be different too!

<br>

