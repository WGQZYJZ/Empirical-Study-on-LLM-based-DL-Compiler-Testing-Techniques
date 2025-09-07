
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(d_model, 4 * d_ff)
        self.fc2 = torch.nn.Linear(4 * d_ff, 2 * d_ff)
        self.fc3 = torch.nn.Linear(2 * d_ff, num_classes)
 
    def forward(self, x):
        # Compute the full sequence-to-sequence embedding using linear layers and residual connections
        x = x + self.emb(x)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(batch_size, max_length, d_model)  # Generate fake input data
output = m(__input__)

