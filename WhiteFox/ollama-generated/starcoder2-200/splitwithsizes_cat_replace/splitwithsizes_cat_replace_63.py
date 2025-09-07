

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
    	splits = torch.split(x1, [50, 47], dim=3)
    	output = torch.cat([splits[i] for i in range(len(splits))], dim=3)
        return output

# Initializing the model
m  = Model()
