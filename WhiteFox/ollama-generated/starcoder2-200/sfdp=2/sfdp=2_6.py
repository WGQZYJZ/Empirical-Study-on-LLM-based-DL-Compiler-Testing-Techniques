
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(32, 768)
        self.key = torch.randn(512, 768)
 
        self.value = torch.randn(512, 1024)
        self.softmax_scale = 6
        
        self.dropout_p =  0.99 # dropout probability

    def forward(self, inputs):
       vq = torch.matmul(inputs, self.query)
       vk = torch.matmul(inputs, self.key).transpose(-2,-1)
       vs = self.softmax_scale * torch.nn.functional.normalize(vk, dim=-1) 
       vd  = torch.nn.functional.dropout(vs, p=self.dropout_p)

       o = vd @ self.value
       return o

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(32,768 )
  