

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): # Forward definition 1

        tensor1 = torch.randn([32])
        tensor2 = torch.randn([64, 50])
        cat_result = torch.cat([tensor1, tensor2], dim=1) 
        reshaped_result = torch.reshape(cat_result,[32, 50 + 1] ) 
        unary_result = torch.relu(reshaped_result)
        return unary_result

# Initializing the model
m  = Model()
__output__  = m(x1)


