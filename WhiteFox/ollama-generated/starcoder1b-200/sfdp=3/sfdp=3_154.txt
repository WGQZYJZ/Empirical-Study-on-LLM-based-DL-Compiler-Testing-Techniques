
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, k1, v1):
        # The scale factor is usually a value between 0 and 1, where the higher the factor, the closer to uniformly distributed distribution we have.
        # In this example, it's 2 in order to preserve the input feature.
        # In our experiment, this parameter should be a carefully tuned.
        scale_factor = 2
        
        k1_scaled = k1.mul(scale_factor)  # Scale the dot product by a factor
        softmax_k1 = k1_scaled.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_k1 = torch.nn.functional.dropout(softmax_k1, p=dropout_p) # Apply dropout to the softmax output
        
        v1_multiplied = v1.matmul(scale_factor)  # Compute the dot product of the dropout output and the value tensor
        output = dropout_k1.matmul(v1_multiplied) # Compute the dot product of the dropout output and the value tensor
 
        return output


# Initializing the model
m = Model()


