

import torch.nn as nn
    
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, input_features=128):
        super().__init__()
        self.input_features = 128
        self.encoder_layer = torch.nn.Linear(128, 768)
        self.decoder_layer = torch.nn.Linear(768, 1000)
 
    def forward(self):
        self._output = self.decoder_layer(torch.relu(self.encoder_layer()))
        return self._output

model = SimpleTransformerModel()

