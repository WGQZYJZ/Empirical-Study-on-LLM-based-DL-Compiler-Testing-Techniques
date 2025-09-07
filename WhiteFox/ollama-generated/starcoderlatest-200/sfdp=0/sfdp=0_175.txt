
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale_factor):
        attention_weights = torch.matmul(query, key.transpose(-2, -1)) / scale_factor
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()


