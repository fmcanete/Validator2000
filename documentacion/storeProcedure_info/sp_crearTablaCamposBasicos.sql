USE [CapturaStratus]
GO
/****** Object:  StoredProcedure [dbo].[sp_crearTablaCamposBasicos]    Script Date: 20/10/2021 21:46:02 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[sp_crearTablaCamposBasicos]
AS



IF EXISTS (select *  from sysobjects where id = object_id('dbo.mov2000_camposBasicos') and sysstat & 0xf = 3)  
--from dbo.mov2000_camposBasicos)                  
 Drop Table dbo.mov2000_camposBasicos 

             

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
	[importe] [float] NULL,
	[codPais] [nchar](10) NULL,
	[importeOrig] [float] NULL,
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
