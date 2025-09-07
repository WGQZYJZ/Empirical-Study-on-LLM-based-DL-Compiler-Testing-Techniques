
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t2  = torch.mm(x1[:,0:4], x1[:,5:9]) # Selecting two rows and four columns from the input tensor 
        t3  = torch.mm(t2, t2)                 # Applying the multiplication to these two rows/columns
        t4  = torch.add(t3[:,0:], x1[:,8:])    # Addition of 1st row of 3rd column and 9th element of every row 
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 5) 
