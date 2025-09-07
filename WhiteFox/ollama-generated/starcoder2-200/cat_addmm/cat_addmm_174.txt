
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear1 = torch.nn.Linear(8 * 32 ** 2 + 456, 790)
        self.linear2 = torch.nn.Linear(790, 444)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1):
       v1 = x1[:, :3 * 8] 
       v1 = v1.view(-1, 8 * 32 ** 2) # reshape the 78x56 input to a tensor with size (2048,)
 
       v2 = x1[:, -456:] 
       v2 = self.linear1(v2) # perform a linear operation on the reshaped 78x56 vector
 
       v3 = torch.cat([v1, v2], dim=1) # concatenate along dimension 0 with the 2048 vector and add it to the vector formed in previous step 
       v3 = self.relu(self.linear2(v3)) 
        return v3

# Initializing the model
m  = Model(-1)


# Inputs to the model
x1   = torch.randn(50, 456 + 8 * 32 ** 2).cuda() # a tensor with size (50, 9784); this is just a placeholder, it should be replaced by the real input 
__output__  = m(x1)

