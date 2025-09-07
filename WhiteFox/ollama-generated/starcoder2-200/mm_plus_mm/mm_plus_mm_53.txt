

class Model(torch.nn.Module):
    def __init__(self, input1=None, input2=None, input3=None, input4=None):
        super().__init__()

    def forward(self, v1: int, v2, v3):
        pass


# Initializing the model
m = Model(input1, input2)

# Inputs to the model
v1  = torch.randn(56*70*84).reshape(39, 56, 70, 84) # shape of input1: [batch_size x n1 x n2 x n3]
v2  = torch.randn(39*56*70*84).reshape(39, 56, 70, 84) # shape of input2: [batch_size x n1 x n2 x n3]
v3  = torch.randn(39*56*70*84).reshape(39, 56, 70, 84) # shape of input3: [batch_size x n1 x n2 x n3]
v4  = torch.randn(39*56*70*84).reshape(39, 56, 70, 84) # shape of input4: [batch_size x n1 x n2 x n3]

# Initializing the model and printing the size of the input tensors. Note that you cannot change these sizes!
m = Model(v1, v2, v3, v4).cuda()
for p in m.parameters():
    print(p.shape)

__output__  = m(torch.ones((56,70)).cuda()) # shape of output: [batch_size x n1 x n2 x n3]