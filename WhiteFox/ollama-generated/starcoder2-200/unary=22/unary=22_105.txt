
class Model(torch.nn.Module):
    def __init__(self, fc1_out, fc2_out):
        super().__init__()

        self.linear = torch.nn.Linear(fc1_out + 4, fc2_out)
 
    def forward(self, x1, x2, x3):
 
        t1  = torch.cat((x1, x2), dim=1).permute(0, 2, 1)
        t2  = self.linear(t1)
        t3  = torch.tanh(t2 + x3[:,None])
        return t3


# Initializing the model with randomized input parameters
fc1_out  = 514 # This value can be replaced by any valid integer.
fc2_out = 78960 # This value can be replaced by any valid integer.

m  = Model(fc1_out, fc2_out)


# Inputs to the model with randomized input parameters