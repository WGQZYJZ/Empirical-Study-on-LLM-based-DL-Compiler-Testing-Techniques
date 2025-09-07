
class Model(torch.nn.Module):
    def __init__(self, in1, in2):
        super().__init__()
        self.m1 = torch.nn.Linear(in1, 5)
        self.m2 = torch.nn.Linear(5, out1)
 
    def forward(self, x1, x2):

        v1 = self.m1(x1)
        v2 = v1 + x2
        return self.m2(v2)


# Initializing the model
m  = Model(in1, in2).cuda()

# Inputs to the model (on GPU tensors only!)
x1 = torch.randn(batch_size//2, num_inputs1)
x2 = torch.randn(batch_size//2, num_inputs2)
 
# Run the model
__output__  = m(x1, x2).cuda()

