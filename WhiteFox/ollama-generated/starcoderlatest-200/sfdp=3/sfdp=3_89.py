
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(256, 8) # hidden size=8
        self.conv_attention = torch.nn.Conv2d(48, 256, 3, stride=1, padding=0)
        self.drop = torch.nn.Dropout(p=dropout_p)
        self.linear2 = torch.nn.Linear(48*4*4, 49*32*32) # hidden size=49

        self.conv_q = torch.nn.Conv2d(1, 16, 1, stride=1, padding=0)
        self.linear3 = torch.nn.Linear(16*4*4, 17*32*32) # hidden size=17

    def forward(self, x1):
        v1 = F.relu(self.drop(self.conv_attention(x1)))
        v2 = self.linear1(v1)
        qk = torch.matmul(v2, v2.transpose(-2,-1)) # Compute the dot product of the query and key tensors

        scaled_qk = qk * scale_factor # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output

        output = torch.matmul(dropout_qk, v2)
        
        output = output.view(-1, 48*4*4).transpose(-1,-2).contiguous()
        wv = self.linear2(output)
        q1 = self.conv_q(x1)
        y1 = self.linear3(q1.view(-1, 16*4*4).transpose(-1,-2).contiguous())

        v1 = torch.cat([wv,y1], dim=0)
        output = F.relu(self.drop(self.conv_attention(v1)))
        v2 = self.linear1(output)
        qk = torch.matmul(v2, v2.transpose(-2,-1)) # Compute the dot product of the query and key tensors

        scaled_qk = qk * scale_factor # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output

        output = torch.matmul(dropout_qk, v2)
        
        output = output.view(-1, 48*4*4).transpose(-1,-2).contiguous()
        wv = self.linear2(output)
        q1 = self.conv_q(x1)
        y1 = self.linear3(q1.view(-1, 16*4*4).transpose(-1,-2).contiguous())

        v2 = torch.cat([wv,y1], dim=0)
        v3 = torch.tanh(v1+v2)
        output = self.linear1(v3)
        return output
