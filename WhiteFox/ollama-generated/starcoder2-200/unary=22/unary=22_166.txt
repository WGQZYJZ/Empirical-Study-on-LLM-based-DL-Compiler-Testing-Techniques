
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64* 32, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1)
        return v2


# Initializing the model and printing its graph
m  = Model()
 
print('Model: ' + str(torch_geometric.utils.dump_to_dot(m)))


