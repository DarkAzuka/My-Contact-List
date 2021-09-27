from django.db import models


class Domicilio(models.Model):
    pais = models.CharField(max_length=255, primary_key=True)
    calle = models.CharField(max_length=255)
    numero_ext = models.IntegerField()
    numero_int = models.IntegerField()

    @property
    def formatoDireccion(self):
        formato_direccion = "Pais, {0} Calle, {1}, Ext: {2}/ Int: {3}"
        return formato_direccion.format(self.pais, self.calle, self.numero_ext, self.numero_int)

    def __str__(self):
        ext = "{0}"
        return ext.format(self.formatoDireccion)


class Persona(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellido_materno = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    domicilio = models.ForeignKey(Domicilio, null=False, blank=False, on_delete=models.CASCADE)

    @property
    def nombreCompleto(self):
        formato_nombre = "{0} {1}, {2}"
        return formato_nombre.format(self.apellido_paterno, self.apellido_materno, self.nombres)

    def __str__(self):
        return f'{self.dni}: {self.nombreCompleto}, {self.sexo}, {self.fecha_nacimiento}'


class Ocupacion(models.Model):
    estatus = [
        ('No', 'Soltero'),
        ('Si', 'Casado'),
    ]
    casado = models.CharField(max_length=2, choices=estatus, default='No')

    ocupaciones = [
        ('Si', 'Si Trabajo'),
        ('No', 'No Trabajo'),
    ]
    trabajo = models.CharField(max_length=2, choices=ocupaciones, default='Si')
    email = models.CharField(max_length=255)

    @property
    def estadoCivil(self):
        formato_civil = "Casado: {}, Actual Trabajando: {}"
        return formato_civil.format(self.casado, self.trabajo)

    def __str__(self):
        txt = 'Estado Civil: {0}, email: {1}'
        return txt.format(self.estadoCivil, self.email)


class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    info_persona = models.ForeignKey(Ocupacion, null=False, blank=False, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_created=True)

    def __str__(self):
        return f'ID: {self.id} Contacto: {self.persona}, ' \
               f'Cotacto: {self.info_persona}, ' \
               f'fecha de Registro: {self.fecha_registro} '
