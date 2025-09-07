
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 5)
 
    def forward(self, x1):

        attention_weights = F.softmax(scaled_dot_product / inv_scale, dim=-2)
        output = attention_weights.matmul(value)
        return self.linear(output), attention_weights

# Initializing the model