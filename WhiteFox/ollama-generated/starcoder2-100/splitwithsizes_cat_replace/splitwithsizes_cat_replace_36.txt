
class Model(torch.nn.Module):
    def __init__(self, num_features, num_labels):
        super().__init__()
        self.dense1 = torch.nn.Linear(num_features, 64)
        self.dense2 = torch.nn.Linear(64, 32)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.dense1(x).view(-1, 500)
        v2 = self.relu(v1)
        v3 = self.relu(v2)
 
        v4 = [
            torch.flatten(v3), 
            torch.sum(torch.stack([self.dense2(v3), v1]), dim=0).view(-1, 64), 
            torch.softmax(torch.matmul(v3, v1), dim=-1).view(-1)
        ]
        
        return sum(v for v in v4)


# Initializing the model and computing its output
model = Model(25 * 9 + 1800, 3)
 
input_tensor = torch.randn([10])
output = model(input_tensor)

