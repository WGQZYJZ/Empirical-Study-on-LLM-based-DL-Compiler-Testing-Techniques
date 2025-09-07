
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.Tensor([10]) # Dummy initialization that scales the output by 10.
 
    def forward(self, x1):
        q = torch.randn((2,3)) 
        k = torch.randn((2,5)) 
        v = torch.randn((2,7)) 
        scaled_dot_product = torch.matmul(q,k.transpose(-2,-1))/torch.sqrt(v.shape[-1])
        attention_weights  = scaled_dot_product.softmax(dim=-1)        
        output = attention_weights.matmul(v)/self.scale # Multiply the softmax attention weights by v and then divide by self.scale to stabilize the gradients.
        return output


# Initializing the model
m = Model()
__output__  = m(x2)


