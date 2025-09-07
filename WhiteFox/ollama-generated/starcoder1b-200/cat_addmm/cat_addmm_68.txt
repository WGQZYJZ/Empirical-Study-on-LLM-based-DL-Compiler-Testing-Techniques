
class Model(torch.nn.Module):
    def __init__(self, n_inputs, n_hidden, n_outputs):
        super().__init__()
        self.conv = torch.nn.Linear(n_inputs, n_hidden)
        self.fc   = torch.nn.Linear(n_hidden, n_outputs)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = self.fc(v1)
        return v2


# Initializing the model
m = Model(n_inputs=3, n_hidden=4, n_outputs=5)

