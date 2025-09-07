
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        query = self.conv1(x)
        key   = self.conv2(x)
        inv_scale  = torch.sqrt(torch.max(query, key, dim=-1)[0] + 1e-12).unsqueeze(-1) # max(query, key) returns the max value along dimension -1 of input tensors x and key. The max value of query is returned as a tensor (tensor([[9, 17]])). So we use torch.max to return the max value.

        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)

        return output


# Initializing the model
m = Model()


