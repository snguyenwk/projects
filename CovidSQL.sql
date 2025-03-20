Select *
From [P1 Portfolio]..CovidDeaths
Where continent is not null
order by 3,4

--Select *
--From [P1 Portfolio]..CovidVac
--order by 3,4

-- Select data that we will be using.

Select Location, date, total_cases, new_cases, total_deaths, population
From [P1 Portfolio]..CovidDeaths
Where continent is not null
order by 1,2

-- Looking at total cases vs total deaths
-- Shows likelihood of dying if you contract COVID-19 in your particular country.

Select Location, date, total_cases, total_deaths, (total_deaths / total_cases) * 100 as DeathPercentage
From [P1 Portfolio]..CovidDeaths
Where location like '%states%'
order by 1,2

-- Total cases vs Population
-- Shows percentage of population that got covid

Select Location, date, population, total_cases, (total_cases / population) * 100 as PopulationCases
From [P1 Portfolio]..CovidDeaths
Where location like '%states%'
order by 1,2

-- Looking at Countries with Highest Infection Rate compared to Population

Select Location, population, MAX(total_cases) as HighestInfectionCount, Max((total_cases / population)) * 100 as PopulationCases
From [P1 Portfolio]..CovidDeaths
--Where location like '%states%'
Group by location, population
order by PopulationCases desc

-- Countries with Highest Death Count per Population

 Select Location, Max(cast(total_deaths as bigint)) as TotalDeathCount
From [P1 Portfolio]..CovidDeaths
--Where location like '%states%'
Where continent is not null
Group by location
order by TotalDeathCount desc

-- Continent Break Down
-- Continents w/ Highest Death Count

 Select continent, Max(cast(total_deaths as bigint)) as TotalDeathCount
From [P1 Portfolio]..CovidDeaths
--Where location like '%states%'
Where continent is not null
Group by continent
order by TotalDeathCount desc

-- GLOBAL NUMBERS

Select date, SUM(new_cases) as total_cases, SUM(cast(new_deaths as bigint)) as total_deaths, SUM(cast(new_deaths as bigint)) / SUM(new_cases) * 100 as DP
From [P1 Portfolio]..CovidDeaths
--Where location like '%states%'
where continent is not null
Group by date
order by 1,2

-- Total Population vs Vaccinations

Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(cast(vac.new_vaccinations as bigint)) OVER (Partition by dea.location Order by dea.location, dea.date) as RollingVaccinations
--, (RollingVaccinations/population) * 100
From [P1 Portfolio]..CovidDeaths dea
Join [P1 Portfolio]..CovidVac vac
	On dea.location = vac.location
	and dea.date = vac.date
	where dea.continent is not null
order by 2, 3

-- USE CTE 

With PopvsVac (continent, location, date, population, new_vaccinations, RollingVaccinations)
as 
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(cast(vac.new_vaccinations as bigint)) OVER (Partition by dea.location Order by dea.location, dea.date) as RollingVaccinations
--, (RollingVaccinations/population) * 100
From [P1 Portfolio]..CovidDeaths dea
Join [P1 Portfolio]..CovidVac vac
	On dea.location = vac.location
	and dea.date = vac.date
	where dea.continent is not null
--order by 2, 3
)

Select *, (RollingVaccinations / Population) * 100
From PopvsVac
