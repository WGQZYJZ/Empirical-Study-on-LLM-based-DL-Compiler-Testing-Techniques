
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        scaled_dot_product  = torch.matmul(input1, input2) / math.sqrt(input3)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(input4)
        return output


# Initializing the model
m = Model()


# Inputs to the model
i1 = torch.randn(5, 2048, 3976)
i2 = torch.randn(5, 3976, 3976)
i3 = 3976
i4 = torch.randn(5, 3976, 2048)


