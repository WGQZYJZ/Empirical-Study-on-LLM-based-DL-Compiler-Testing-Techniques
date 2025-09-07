
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(784, 30)
        self.m2 = torch.nn.Linear(30, 5)
 
    def forward(self, x):
         v_out = self.m1(x)
         v_out = F.softmax(v_out, dim=1)
         return v_out


# Initializing the model and getting a sample input of shape [batchsize x 784] for the model inputs
m = Model()
inputdata  = torch.randn(500, 30)


# Generate a single output using random weights for every operation in the model.

random_weight = torch.rand([792], requires_grad=True).to("cuda")
random_weight.requires_grad_(True)
__output__  = m(inputdata)

# Printing outputs from the Model.
print("__output__: " + str(__output__))

