
class TransformerModel(torch.nn.Module):
    def __init__(self, config: Union[dict]):
        super().__init__()

        self.dropout = torch.nn.Dropout(config["dropout"])
 
        self.encoder = TransformerEncoder(config)
        self.decoder = TransformerDecoder(config)

    def forward_step(self, hidden_states):
        layer1  = self.encoder(hidden_states[0], mask=hidden_states[2]) 
        layer1  = tuple(self.dropout(layer1)) + (layer1,)
 
        layer1  = self.decoder(hidden_states[3][0], mask=hidden_states[5], hidden_state=layer1)
        layer1  = self.dropout(layer1)
        layer2, layer3  = tuple(hidden_states[4]), tuple(hidden_states[6])
 
        layer1  = layer1 + (layer3,)
        layer1  = layer1[:2]
        layer1 += [layer2[0]]
        layer1  = tuple(layer1)

        return layer1

