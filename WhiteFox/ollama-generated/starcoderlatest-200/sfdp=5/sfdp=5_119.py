
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 64)
 
    def forward(self, x1):
        v1 = x1 @ self.linear.weight.transpose(-2, -1) / math.sqrt(x1.size(-1)) + \
              self.linear.bias.view(*self.linear.bias.shape[:-1])  # Compute the dot product of the query and key, and scale it
        v2 = torch.softmax(v1, dim=-1)
        v3 = torch.dropout(v2, dropout_p, True)
        output = v3 @ self.linear.weight + self.linear.bias  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()
