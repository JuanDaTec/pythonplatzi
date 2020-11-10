class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        """
        Definiendo el constructor.
        """
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        """
        Getter
        Se usa el decorador @property para señalar que es el metodo get
        """
        return self._region
    
    @region.setter
    def set_region(self, region):
        """
        Setter
        Se usa el decorador @region.setter para señalar que es el metodo setter
        """
        if region in self._pais:
            self._region=region

            raise ValueError(f'La region {region} no es valida en {self._pais}')

casilla = CasillaDeVotacion (1,['Colombia, Perú'])
casilla.region = 'Colombia'
print (casilla.region)