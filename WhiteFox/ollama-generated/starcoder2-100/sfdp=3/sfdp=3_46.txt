
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.functional.linear
 
        self.scale_factor  = scale_factor

        # Generate this factor randomly. You may want to put it into a variable, or initialize it in the model initialization code.
        # For example, scale_factor += 5 * torch.randn(1)
        scale_factor = 3
    
        self.dropout_p = dropout_p
    
        # Generate these two tensors randomly. You may want to put them in variables, or initialize them in the model initialization code.
        # For example, query = torch.nn.Parameter(torch.rand(2048))
        #         value = torch.nn.Parameter(torch.rand(512, 2048))
        query  = torch.nn.Parameter(torch.randn(32768)) 
        key    = torch.nn.Parameter(torch.randn(32768, 32768))
        value  = torch.nn.Parameter(torch.randn(1024, 32768))
    
    def forward(self):
        v0  = self.matmul(query, key.transpose(-2, -1) * scale_factor)
        v1  = v0.softmax(dim=-1)
        v2  = torch.nn.functional.dropout(v1, p=dropout_p) 
        return v2.matmul(value),


# Initializing the model
m  = Model()

# Inputs to the model
__output__, = m()
