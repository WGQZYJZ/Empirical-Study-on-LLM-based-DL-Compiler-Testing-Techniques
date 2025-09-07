
class Model(torch.nn.Module):
    def __init__(self, k, d):
        super().__init__()
        self.split = torch.split(input_tensor, k)

    def forward(self):
        return torch.cat([self.split[i] for i in range(len(k))], dim=1)

# Initializing the model
m  = Model(4, 0)
