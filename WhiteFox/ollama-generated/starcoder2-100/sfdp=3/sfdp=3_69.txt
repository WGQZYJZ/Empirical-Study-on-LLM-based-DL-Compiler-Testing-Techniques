
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk, k, v):
 
        scale_factor  = self._scale_factor() # Scaling the dot product by a factor
        scaled_qk  = torch.matmul(qk, k.transpose(-2,-1)) * scale_factor
 
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self._dropout()) # Applying the dropout
        
        output = dropout_qk.matmul(v)
        return output

    def _scale_factor(self):
        return self.get_state()['scale']
 
    def get_state(self):
        return {
            'scale': random(),
            'drop' : random()
        }

    def _dropout(self):
        return self.get_state()['drop']

# Initializing the model
m = Model()
qk  = torch.randn([32,640]) # Creating a random query tensor of shape [B, Sq]
key  = torch.randn([512,8]) # Creating a random key tensor of shape [Bk, Sk]
value = torch.randn([32,512,8]) # Creating a random value tensor of shape [B, Sv, V]
 
output = m(qk,key,value)

