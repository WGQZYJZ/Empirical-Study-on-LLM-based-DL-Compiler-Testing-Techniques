
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / np.sqrt(np.max(np.abs(x1), np.abs(x2)))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x2)
        return output


# Initializing the model
m = Model()


