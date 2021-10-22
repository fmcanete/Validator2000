USE [CapturaStratus]
GO

/****** Object:  Table [dbo].[mov2000_camposBasicos]    Script Date: 20/10/2021 16:17:48 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[mov2000_camposBasicos](
	[idTrx] int IDENTITY (1,1) NOT NULL,
	[numTarMovMes] [nvarchar](20) NULL,
	[establecimiento] [nchar](10) NULL,
	[nroAut] [nchar](10) NULL,
	[planCuot] [nchar](10) NULL,
	[numCuot] [nchar](10) NULL,
	[cuotas] [nchar](10) NULL,
	[AjusteCuota1STD] [nchar](10) NULL,
	[moneda] [nchar](10) NULL,
	[importe] [nchar](10) NULL,
	[codPais] [nchar](10) NULL,
	[importeOrig] [nchar](10) NULL,
	[binBancoPagador] [nchar](10) NULL,
	[nombreComercio] [nvarchar](50) NULL,
	[TjCodBanco] [nchar](10) NULL,
	[numTarMov2000] [nvarchar](20) NULL,
	[planGob] [nchar](10) NULL,
	[token] [nchar](10) NULL,
	[numToken] [nvarchar](20) NULL,
	[posDataCode] [nvarchar](20) NULL,
	[visaRelease] [nchar](10) NULL,
	[tipoTarjeta] [nchar](10) NULL,
	[campoBCRA] [nchar](10) NULL,
	[diasPago] [nchar](10) NULL,
 CONSTRAINT [PK_Table_1] PRIMARY KEY CLUSTERED 
(
	[idTrx] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


 