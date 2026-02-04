/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2019 OpenCFD Ltd.
    Copyright (C) YEAR AUTHOR, AFFILIATION
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

\*---------------------------------------------------------------------------*/

#include "fixedValueFvPatchFieldTemplate.H"
#include "addToRunTimeSelectionTable.H"
#include "fvPatchFieldMapper.H"
#include "volFields.H"
#include "surfaceFields.H"
#include "unitConversion.H"

//{{{ begin codeInclude

//}}} end codeInclude


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

// dynamicCode:
// SHA1 = 3f68d5b585f47114f3e2502653e76b5ee1106162
//
// unique function name that can be checked if the correct library version
// has been loaded
extern "C" void swirl_3f68d5b585f47114f3e2502653e76b5ee1106162(bool load)
{
    if (load)
    {
        // Code that can be explicitly executed after loading
    }
    else
    {
        // Code that can be explicitly executed before unloading
    }
}

// * * * * * * * * * * * * * * Static Data Members * * * * * * * * * * * * * //

makeRemovablePatchTypeField
(
    fvPatchVectorField,
    swirlFixedValueFvPatchVectorField
);


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

swirlFixedValueFvPatchVectorField::
swirlFixedValueFvPatchVectorField
(
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF
)
:
    fixedValueFvPatchField<vector>(p, iF)
{
    if (false)
    {
        printMessage("Construct swirl : patch/DimensionedField");
    }
}


swirlFixedValueFvPatchVectorField::
swirlFixedValueFvPatchVectorField
(
    const swirlFixedValueFvPatchVectorField& ptf,
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF,
    const fvPatchFieldMapper& mapper
)
:
    fixedValueFvPatchField<vector>(ptf, p, iF, mapper)
{
    if (false)
    {
        printMessage("Construct swirl : patch/DimensionedField/mapper");
    }
}


swirlFixedValueFvPatchVectorField::
swirlFixedValueFvPatchVectorField
(
    const fvPatch& p,
    const DimensionedField<vector, volMesh>& iF,
    const dictionary& dict
)
:
    fixedValueFvPatchField<vector>(p, iF, dict)
{
    if (false)
    {
        printMessage("Construct swirl : patch/dictionary");
    }
}


swirlFixedValueFvPatchVectorField::
swirlFixedValueFvPatchVectorField
(
    const swirlFixedValueFvPatchVectorField& ptf
)
:
    fixedValueFvPatchField<vector>(ptf)
{
    if (false)
    {
        printMessage("Copy construct swirl");
    }
}


swirlFixedValueFvPatchVectorField::
swirlFixedValueFvPatchVectorField
(
    const swirlFixedValueFvPatchVectorField& ptf,
    const DimensionedField<vector, volMesh>& iF
)
:
    fixedValueFvPatchField<vector>(ptf, iF)
{
    if (false)
    {
        printMessage("Construct swirl : copy/DimensionedField");
    }
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

swirlFixedValueFvPatchVectorField::
~swirlFixedValueFvPatchVectorField()
{
    if (false)
    {
        printMessage("Destroy swirl");
    }
}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void swirlFixedValueFvPatchVectorField::updateCoeffs()
{
    if (this->updated())
    {
        return;
    }

    if (false)
    {
        printMessage("updateCoeffs swirl");
    }

//{{{ begin code
    #line 32 "/mnt/mace01-rds/thermofluids/impJetAM/pipeCyclic/0/U.boundaryField.inlet"
// Uncomment for testing on non-windows systems [fragile]
            // IOobject::scopeSeparator = '_';

            const vector axis(1, 0, 0);

            vectorField v(2.0*this->patch().Cf() ^ axis);
            v.replace(vector::X, 1.0);
            operator==(v);
//}}} end code

    this->fixedValueFvPatchField<vector>::updateCoeffs();
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

