
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(5, 64)
        self.fc2 = torch.nn.Linear(64, 64)
 
    def forward(self, x1, x2):
        query_layer = self.fc1(x1)
        key_layer = self.fc2(x2)
 
        v1 = torch.matmul(query_layer, key_layer)
        v1 = v1 + 1e-5  # Prevent dividing by zero
        v1 = torch.softmax(v1, dim=-1)
        v2 = torch.matmul(v1, value)
        output = v2 @ key_weights
 
        return output


# Initializing the model
m = Model()


