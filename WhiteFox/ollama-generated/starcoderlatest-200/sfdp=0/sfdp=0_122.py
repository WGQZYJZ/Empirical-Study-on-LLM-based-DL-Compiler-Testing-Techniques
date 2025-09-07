
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 128)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / (0.5 * math.sqrt(32))
        attention_weights = torch.softmax(scaled_dot_product, dim=-1)
        output = attention_weights.matmul(x1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
a = torch.randn(64 * 64 * 3, 20) # (h*w*c) x num_heads -> (h x w x c) x num_heads
        b = torch.randn(1, 8, 64, 64)
