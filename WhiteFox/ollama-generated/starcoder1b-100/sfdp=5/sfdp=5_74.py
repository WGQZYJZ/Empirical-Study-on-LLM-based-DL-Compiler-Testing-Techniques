
class Model(torch.nn.Module):
    def __init__(self, input_size, embed_size=128, hidden_dim=512):
        super().__init__()

        self.fc = torch.nn.Linear(input_size, hidden_dim)
        self.linear = torch.nn.Linear(hidden_dim, 3)

    def forward(self, x1, x2, x3):
        x = F.relu(self.fc(x1))

        # Here the linear layers are replaced with an attention mechanism to compute attention weights of all tokens in a word. 
        x = self.linear(F.relu(self.fc(x2)))
        x = self.linear(F.relu(self.fc(x3)))

        return F.softmax(output, dim=-1)

    def load_state_dict(self, dict):
        super().load_state_dict(dict)
        for param in self.parameters():
            if 'weight' in param.name:
                param.data = param.data * 2

# Initializing the model
m = Model(input_size=16)

# Inputs to the model
x1 = torch.randn(3, 8, 4, 4)
x2 = torch.randn(3, 8, 128, 64)
x3 = torch.randn(3, 8, 64, 512)
