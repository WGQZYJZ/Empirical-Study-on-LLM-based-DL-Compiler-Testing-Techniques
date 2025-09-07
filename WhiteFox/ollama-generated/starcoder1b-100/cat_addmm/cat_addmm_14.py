
class Model(torch.nn.Module):
    def __init__(self, num_hidden):
        super().__init__()
        self.num_layers = 2
        hidden_layers = torch.nn.ModuleList()
        for i in range(self.num_layers):
            layer = torch.nn.Linear(10, 3)
            layer.bias.data = torch.zeros(layer.bias.size(), dtype=torch.float32).cuda()
            hidden_layers.append(layer)
        
        self.fc1 = torch.nn.Linear(784, 50)
        self.fc2 = torch.nn.Linear(50, num_hidden)
 
    def forward(self, x):
        layer_list = [self.fc1, self.fc2]
        for layer in layer_list:
            x = F.relu(layer(x))
 
        x = F.log_softmax(layer_list[-1](x), dim=0)
        return x


# Initializing the model
m = Model(num_hidden)


# Inputs to the model
x  = torch.randn(2, 784)
