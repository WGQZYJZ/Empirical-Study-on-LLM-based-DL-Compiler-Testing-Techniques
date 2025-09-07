
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1, value2):
        scaled_dot_product = torch.matmul(query1, value2) / math.sqrt(value2.shape[-1])
        attention_weights  = scaled_dot_product.softmax(dim=-1)

        output = attention_weights @ query1

        return output

# Initializing the model
m = Model()

