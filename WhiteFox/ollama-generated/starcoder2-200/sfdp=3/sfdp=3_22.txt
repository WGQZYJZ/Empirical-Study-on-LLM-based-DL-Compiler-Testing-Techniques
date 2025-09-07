
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.randn(512, 64) # 512 * 64 size query tensor
        self.key = torch.randn(512, 8)  # 512 * 8 size key tensor
        self.value = torch.randn(512, 70)  # 512 * 70 size value tensor
        self.scale_factor = float(torch.randint(499, high=4999)) / 100.0 
        self.dropout_p = float(torch.randint(low=32,high=64))/80 # A randomly selected dropout parameter
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self):
         qk  =  torch.matmul(self.query, self.key.transpose(-2, -1)) 
         scaled_qk  = qk.mul(scale_factor)
         softmax_qk = self.softmax(scaled_qk)
         dropout_qk  =  torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
         output  = dropout_qk.matmul(value)
         return output

 # Initializing the model
 m  = Model()
 
# Inputs to the model 
 __output__  = m()
 
 