
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.softmax = torch.nn.Softmax()

    def forward(self, x1, k, v):
        v1 = self.conv(x1)
        query  = v1.unsqueeze(-2).repeat((1, k.shape[0], 1))  # Add batch dimension for the two tensors
        key    = torch.matmul(v1, k) / (self.softmax(k).unsqueeze(-1).unsqueeze(-2).expand_as(key))
        attention_weights  = self.softmax(torch.matmul(query, key.transpose(-2, -1)))
        output  = torch.matmul(attention_weights, v1)
        return output

# Initializing the model
m = Model()


