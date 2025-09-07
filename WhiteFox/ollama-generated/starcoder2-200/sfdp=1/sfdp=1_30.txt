
class Model(torch.nn.Module):
    def __init__(self, scale=1., dropout=0.5):
        super().__init__()
        self.scale = 1./math.sqrt(scale)
        self.inv_scale_factor = torch.tensor([self.scale])
 
        self.key = torch.nn.Linear(in_features=768, out_features=768) 
        self.query = torch.nn.Linear(in_features=768, out_features=768)
        self.value = torch.nn.Linear(in_features=768, out_features=768)
 
        self.dropout  = torch.nn.Dropout(p=0.5, inplace=False)

    def forward(self, query):
        key = self.key(query).view(-1, 4399, -1) # [1, 4399, 768]
        value = self.value(query).view(-1, 4399, -1) 
        
        q = self.scale_factor_fn(self.query(query), self.scale_factor) # [4399, 4399]
        k = self.scale_factor_fn(self.key(key).transpose(-2,-1), self.scale_factor) # [4399, 768*768]
        
        # Compute the dot product of the query and key tensors
        qk = torch.matmul(q, k) 
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk  = self.dropout(softmax_qk)

        # Compute the dot product of the dropout output and the value tensor
        output = torch.bmm(dropout_qk, value).view(-1, 768)
 
        return output

# Initializing the model
scale = .5; scale = int(scale * math.sqrt(3)); print("scale: ", scale)
m  = Model(scale=float(scale), dropout=.2)

 # Inputs to the model
query  = torch.randn(1,4798).to(dtype=torch.get_default_dtype())

 __output__  = m(query)

