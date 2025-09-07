
class Model(torch.nn.Module):
    def __init__(self, d_in, d_out, num_layers=1):
        super().__init__()
        self.layers = torch.nn.Sequential(*[
            torch.nn.Linear(d_in, d_out) for i in range(num_layers - 2)])
 
    def forward(self, x1, x2):
        return self.layers(torch.cat([x1, x2], dim=1))


# Initializing the model
m = Model(3, 6, num_layers=3)


