
class Model(torch.nn.Module):
    def __init__(self, num_features=64):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv1(x)
        w = self.conv2(v)
        w_norm = F.normalize(w, p=2, dim=-1) # Normalization to reduce over time dimensions
        v_norm = torch.einsum('bij,bkj->bj', (w, x)) # Compute the dot product of the weights and input vectors
        scaled_v_norm = v_norm * scale
        output = F.softmax(scaled_v_norm, dim=-1)
        output = output.matmul(value)
        return output


# Initializing the model
m = Model()

