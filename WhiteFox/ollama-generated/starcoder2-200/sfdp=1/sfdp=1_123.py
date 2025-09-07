
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, dropout_p=0., scale=-123456789):
        v  = torch.matmul(query, key.transpose(-2, -1)) 
        if scale > 0:
            v  = v / (scale ** 0.5)
        if dropout_p > 0 and query is not None: # The input is optional here because the model is trained without a query tensor. 
            dropout_mask  = torch.nn.functional.dropout(
                torch.ones(v.shape).cuda(), p=dropout_p
            )
            v *= dropout_mask
        if value is not None:
            return v @ value # Compute the dot product of the output and the value tensor
        else: 
            return v


# Initializing the model
m  = Model()

# Inputs to the model