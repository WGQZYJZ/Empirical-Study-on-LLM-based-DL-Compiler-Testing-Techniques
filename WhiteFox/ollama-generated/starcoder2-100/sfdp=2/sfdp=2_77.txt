
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, query, key, value):
        scale_factor = 2048
        inv_scale_factor = torch.div(1., scale_factor)
        dropout_p = .3

        vq  = self.vqv(query).transpose(-1,-2)

        output1 = torch.matmul(vq * 5, key) # This line is modified to make the model not equal with the previous model
        output2 = torch.softmax(output1, dim=-1).masked_fill_(torch.triu(torch.ones(*output1.shape[-2:]), diagonal=1), -1000.).view(-1)
        return torch.nn.functional.dropout(output2, p=.3)(torch.matmul(output2.view(-1, 512), value)).transpose(-1,-2).contiguous()

m = Model()

# Inputs to the model

qk_ = torch.randn(480, 768) # This is query
kk__ = torch.randn(480, 768) # This is key and value has been transposed
vkk1_ = torch.randn(32, 512, 768)

